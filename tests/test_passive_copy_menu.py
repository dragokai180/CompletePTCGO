"""Passive attack grants use the native paged copy-attack picker."""
import unittest
import uuid
from unittest.mock import AsyncMock, patch

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Attack
from spirit.game.session.effects import AttackContext, resolve_attack
from spirit.game.session.legal_actions import (
    PASSIVE_COPY_ATTACK, compute_legal_actions, copy_attack_choice_node,
    passive_copy_candidates,
)
from spirit.game.session.passives import granted_extra_attack_choices
from spirit.tools.effect_smoke import P1, P2
from tests import test_hgss_rules as fixtures


class PassiveCopyMenuTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_twelve_copied_attacks_use_one_paged_menu_row(self):
        rig, entities = self.rig('BW6.MewEX_46')
        active = entities['target']
        rig.session.turn_state.turn_number = 3
        pairs = []
        for index in range(12):
            attack = Attack(title=f'Copied {index}')
            attack.ability_id = str(uuid.uuid4())
            pairs.append((entities['p2_active'], attack))

        with patch('spirit.game.session.legal_actions.granted_extra_attack_choices',
                   return_value=pairs):
            candidates = passive_copy_candidates(rig.board, rig.session.turn_state, P1)
            rows = rig.session._pie_ability_entries(active)

        self.assertEqual(len(candidates), 12)
        attack_rows = [row for row in rows if row['abilityType'] == 'Attack']
        self.assertEqual(len(attack_rows), 2)  # Mew's Replace + the menu
        self.assertEqual(attack_rows[-1]['abilityID'], PASSIVE_COPY_ATTACK.ability_id)
        active.set_attribute(AttrID.PIE_ABILITIES, rows)
        actions = compute_legal_actions(
            rig.board, rig.session.turn_state, P1, rig.session.game_id
        )
        self.assertTrue(any(
            entry['selectableAction']['actionID'] == PASSIVE_COPY_ATTACK.ability_id
            for entry in actions
        ))
        node = copy_attack_choice_node(active.entity_id, candidates)
        self.assertEqual(len(node['choices']), 12)
        self.assertEqual(node['choices'][11]['title']['id'], 'Copied 11')

    async def test_menu_can_select_last_attack_and_filters_ineligible_ones(self):
        rig, entities = self.rig('BW6.MewEX_46')
        active = entities['target']
        rig.session.turn_state.turn_number = 3
        free = [Attack(title=f'Free {index}') for index in range(12)]
        for attack in free:
            attack.ability_id = str(uuid.uuid4())
        expensive = Attack(title='Expensive', cost={PokemonTypes.DRAGON: 99})
        expensive.ability_id = str(uuid.uuid4())
        used_gx = Attack(title='Spent GX', gx=True)
        used_gx.ability_id = str(uuid.uuid4())
        rig.session.turn_state.gx_used.add(P1)
        pairs = [(entities['p2_active'], attack)
                 for attack in (*free, expensive, used_gx)]

        with patch('spirit.game.session.legal_actions.granted_extra_attack_choices',
                   return_value=pairs):
            self.assertEqual(
                [attack.title for _, attack in passive_copy_candidates(
                    rig.board, rig.session.turn_state, P1)],
                [attack.title for attack in free]
            )
            ctx = AttackContext(rig.session, P1, active, PASSIVE_COPY_ATTACK)
            rig.session.prompt_attack_selection = AsyncMock(return_value=11)
            ctx.use_attack = AsyncMock()
            await PASSIVE_COPY_ATTACK.effect(ctx)

        rig.session.prompt_attack_selection.assert_awaited_once()
        self.assertEqual(len(rig.session.prompt_attack_selection.call_args.args[2]), 12)
        ctx.use_attack.assert_awaited_once_with(free[11])

    async def test_resolved_copy_records_the_attack_chosen(self):
        rig, entities = self.rig('BW6.MewEX_46')
        rig.session.turn_state.turn_number = 3

        async def no_effect(ctx):
            return None

        chosen = Attack(title='Actual copied attack', effect=no_effect)
        chosen.ability_id = str(uuid.uuid4())
        pair = (entities['p2_active'], chosen)
        rig.session.prompt_attack_selection = AsyncMock(return_value=0)
        with patch('spirit.game.session.legal_actions.granted_extra_attack_choices',
                   return_value=[pair]), \
             patch('spirit.game.session.effects._send_attack_bracket',
                   new_callable=AsyncMock), \
             patch('spirit.game.session.effects._run_attack_followups',
                   new_callable=AsyncMock):
            await resolve_attack(
                rig.session, P1, entities['target'], PASSIVE_COPY_ATTACK,
                PASSIVE_COPY_ATTACK.ability_id,
            )
        self.assertEqual(rig.session.turn_state.attacks_used[-1][2], chosen.title)

    def test_real_passives_keep_original_attack_owner(self):
        for copier, source, zone, owner in (
            ('BW6.MewEX_46', 'ME55.Pikachuex_53', 'bench', P2),
            ('ME55.Mewex_66', 'ME55.Pikachuex_53', 'bench', P1),
            ('PGO.Ditto_53', 'HGSS1.Pikachu_78', 'discard', P1),
            ('HGSS4.Mew_97', 'HGSS1.Pikachu_78', 'lostZone', P1),
            ('Promo_SM.MewtwoMewGX_191', 'SM3.MarshadowGX_80', 'bench', P1),
            ('SM3.MarshadowGX_80', 'HGSS1.Pikachu_78', 'discard', P1),
            ('XY10.Mew_29', 'HGSS1.Pikachu_78', 'bench', P1),
            ('Promo_XY.Ditto_40', 'HGSS1.Pikachu_78', 'activePokemonArea', P2),
        ):
            with self.subTest(copier=copier):
                rig, entities = self.rig(copier)
                if zone == 'activePokemonArea':
                    rig.to_area(entities['p2_active'], P2, 'bench')
                card = self.add(rig, fixtures.definition(source), owner, zone)
                choices = granted_extra_attack_choices(rig.board, entities['target'])
                self.assertTrue(any(actual is card for actual, _ in choices))
                self.assertTrue(all(attack.ability_id for _, attack in choices))


if __name__ == '__main__':
    unittest.main()
