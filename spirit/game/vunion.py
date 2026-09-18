"""Native four-part V-UNION cards. Fragments and assembled Pokemon are distinct.

Only fragments are collectible. The runtime definition is registered for rules,
but never added to the collection/deck catalog. Its wire archetype references a
real fragment; all assembled characteristics and the native combined texture
are carried in EntityIntroduced, just as for other generated in-play entities.
"""
import uuid

from spirit.game.attributes import (
    AttrID, GameSequence, PokemonStage, PokemonTypes as T, Rarities,
    SpecialConditions, TrainerType, FoilEffects,
)
from spirit.network.message_names import OutboundMsg
from spirit.game.data_utils import (
    Ability, Activations, Attack, PokemonCardDef, Foil, def_for,
    CARD_DEFS_BY_GUID, RUNTIME_CARD_DEFS_BY_GUID,
)
from spirit.game.models.board import CompositePokemonEntity
from spirit.game.models.card import PokemonCard
from spirit.game.session.passives import (
    Passive, effective_bench_capacity, pokemon_entry_blocked, energy_provided_options,
)


# start, type, HP, weakness, resistance, native V-UNION family, original bundle
SPECS = {
    'Pikachu': (139, T.LIGHTNING, 300, T.FIGHTING, T.UNSET, 915, 'lightning_CRR84_7'),
    'Greninja': (155, T.WATER, 300, T.LIGHTNING, T.UNSET, 916, 'water_CRR83_2'),
    'Mewtwo': (159, T.PSYCHIC, 300, T.DARKNESS, T.FIGHTING, 917, 'psychic_CRR83_3'),
    'Zacian': (163, T.METAL, 320, T.FIRE, T.GRASS, 918, 'metal_CRR83_3'),
    'Morpeko': (215, T.LIGHTNING, 310, T.FIGHTING, T.UNSET, 973, 'lightning_CRR88_2'),
}
# Native AttributeDB identities, matched to collector numbers in the original
# Rotom Promo_SWSH export (18b7dccc078300c1b1d82029e4a4dfb4). Each print uses
# Holo/SunPillar, intensity 201; these are not inferred V/VMAX fallback foils.
NATIVE_GUIDS = {
    139: '0265b103-fd5c-4d25-bb75-83ba391a6f1e',
    140: 'bb7882c7-deda-4abd-841f-49ba9f63d3f8',
    141: 'ffbfa0b3-7fb5-436f-99b3-44609c2ad2f8',
    142: '24c3a70e-3c49-4dfe-93cb-8cd51872903e',
    155: 'a7390c5c-3f4f-4423-bac1-851ab5d6c3bd',
    156: '56c855fe-0f28-4338-be8a-a8764b777a51',
    157: 'f220b9b7-e21b-4e82-b26a-b1044bb7e1fd',
    158: '391368cd-1d05-4796-aaf0-7810eda883c8',
    159: 'f5b0de36-a55d-4a2d-87aa-4c2ba1248d0d',
    160: '90c1d898-1a46-4e36-93c2-e803358dbb36',
    161: '717dc235-e0d6-4c27-81b6-258263455ff6',
    162: 'fe6dd13e-a0b4-4737-9a15-0a45446199ca',
    163: '64204cdb-c391-4558-b956-113a4ff27a91',
    164: 'c23bb3ba-b548-4f66-8a02-7a199a8d1e27',
    165: '21ba734d-0f6a-4c4d-bbce-c3e4e47b0c2f',
    166: 'c0a816f6-3cd6-4381-ab34-4a73ab416a5d',
    215: 'c41dcad4-e976-48ca-b2ab-126634d2fe1f',
    216: '95e37d14-0223-4ab8-834d-9244da9ff11b',
    217: '8dce272a-90f1-42a1-aa8c-392ae579dce5',
    218: 'a9d18b14-c09b-4b9f-ab53-d7a425e4967a',
}
_RUNTIME = {}


class NinjaBody(Passive):
    def blocks_trainer_effects(self, affected_player_id, trainer_card, trainer_type,
                              carrier, affected_entity=None, board=None):
        return (trainer_card.owning_player_id != carrier.owning_player_id
                and trainer_type == TrainerType.ITEM
                and (affected_entity is carrier
                     or getattr(affected_entity, 'parent', None) is carrier))


class AntidoteJutsu(Passive):
    def blocks_special_conditions(self, target, condition, carrier):
        return target is carrier and condition == SpecialConditions.POISONED


class PhotonBarrier(Passive):
    def blocks_attack_effects(self, target, carrier):
        return target is carrier


class CrownedSword(Passive):
    def modify_damage_dealt(self, calc, carrier):
        if calc.is_attack and calc.attacker is carrier:
            calc.amount = max(0, calc.amount - 150)


async def union_gain(ctx):
    from spirit.game.session.effects import is_energy_card
    # The printed type belongs to this attack, not to a Pokemon copying it.
    energy_type = ctx.ability.vunion_energy_type
    pool = [card for card in ctx.discard_pile() if is_energy_card(card)
            and any(energy_type.value in option for option in energy_provided_options(ctx.board, card))]
    if pool:
        picked = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0,
                                        prompt='Attach up to 2 Energy cards to this Pokemon')
        for card in picked:
            await ctx.attach_energy(card, ctx.source)


async def shocking_shock(ctx):
    await ctx.deal_damage()
    if (await ctx.flip_coins(1))[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


async def disconnect(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id,
                   lambda card: card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.ITEM)


async def feel_the_way(ctx):
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)


async def twister_shuriken(ctx):
    for pokemon in list(ctx.opponent_bench()):
        await ctx.deal_damage(100, pokemon, apply_modifiers=False)


async def waterfall_blind(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None:
        ctx.lock_retreat(ctx.defender)


async def super_regeneration(ctx):
    await ctx.heal(200, ctx.source)


async def psysplosion(ctx):
    await ctx.place_damage_counters(16)


async def crowned_sword(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None:
        ctx.add_passive_through_opponents_turn(ctx.defender, CrownedSword())


async def master_blade(ctx):
    await ctx.deal_damage()
    await ctx.discard_energy_units_from(ctx.source, 3, partial=True)


async def all_you_can_eat(ctx):
    await ctx.draw_until(10)


async def burst_wheel(ctx):
    energies = list(ctx.attached_energies(ctx.source))
    await ctx.discard_cards(energies)
    discarded = [e for e in energies if e._containing_area_name() == 'discard']
    await ctx.deal_damage(100 * len(discarded))


def attacks_and_abilities(name):
    kind = SPECS[name][1]
    gain = Attack(title='Union Gain', cost={T.COLORLESS: 1}, damage=0,
                  game_text=f'Attach up to 2 {kind.name.title()} Energy cards from your discard pile to this Pokemon.',
                  effect=union_gain)
    gain.vunion_energy_type = kind
    if name == 'Pikachu':
        return [gain,
            Attack(title='Shocking Shock', cost={T.LIGHTNING: 1, T.COLORLESS: 1}, damage=120,
                   game_text="Flip a coin. If heads, your opponent's Active Pokemon is now Paralyzed.", effect=shocking_shock),
            Attack(title='Disconnect', cost={T.LIGHTNING: 2, T.COLORLESS: 1}, damage=150,
                   game_text="During your opponent's next turn, they can't play any Item cards from their hand.", effect=disconnect),
            Attack(title='Electro Ball Together', cost={T.LIGHTNING: 2, T.COLORLESS: 1}, damage=250)]
    if name == 'Greninja':
        return [
            Ability(title='Ninja Body', game_text="Whenever your opponent plays an Item card from their hand, prevent all effects of that card done to this Pokemon.", passive=NinjaBody()),
            Ability(title='Antidote Jutsu', game_text="This Pokemon can't be Poisoned.", passive=AntidoteJutsu()),
            Ability(title='Feel the Way', game_text="Once during your turn, you may have your opponent reveal their hand.",
                    activation=Activations.ONCE_PER_TURN, effect=feel_the_way,
                    condition=lambda board, pid, source: source in board.pokemon_in_play(pid)
                    and bool(board.find_player_area(next(p for p in board.player_ids if p != pid), 'hand').children)),
            gain, Attack(title='Aqua Edge', cost={T.WATER: 1}, damage=130),
            Attack(title='Twister Shuriken', cost={T.WATER: 2, T.COLORLESS: 1}, damage=0,
                   game_text="This attack does 100 damage to each of your opponent's Benched Pokemon. (Don't apply Weakness and Resistance for Benched Pokemon.)", effect=twister_shuriken),
            Attack(title='Waterfall Blind', cost={T.WATER: 2, T.COLORLESS: 1}, damage=180,
                   game_text="During your opponent's next turn, the Defending Pokemon can't retreat.", effect=waterfall_blind)]
    if name == 'Mewtwo':
        return [Ability(title='Photon Barrier', game_text="Prevent all effects of attacks from your opponent's Pokemon done to this Pokemon. (Damage is not an effect.)", passive=PhotonBarrier()),
            gain, Attack(title='Super Regeneration', cost={T.PSYCHIC: 2, T.COLORLESS: 1}, damage=0,
                         game_text='Heal 200 damage from this Pokemon.', effect=super_regeneration),
            Attack(title='Psysplosion', cost={T.PSYCHIC: 2, T.COLORLESS: 1}, damage=0,
                   game_text="Put 16 damage counters on your opponent's Pokemon in any way you like.", effect=psysplosion),
            Attack(title='Final Burn', cost={T.PSYCHIC: 3, T.COLORLESS: 1}, damage=300)]
    if name == 'Zacian':
        return [gain, Attack(title='Dance of the Crowned Sword', cost={T.METAL: 2, T.COLORLESS: 1}, damage=150,
                    game_text="During your opponent's next turn, the Defending Pokemon's attacks do 150 less damage (before applying Weakness and Resistance).", effect=crowned_sword),
            Attack(title='Steel Cut', cost={T.METAL: 2, T.COLORLESS: 1}, damage=200),
            Attack(title='Master Blade', cost={T.METAL: 3, T.COLORLESS: 1}, damage=340,
                   game_text='Discard 3 Energy from this Pokemon.', effect=master_blade)]
    return [gain, Attack(title='All You Can Eat', cost={T.COLORLESS: 2}, damage=0,
                        game_text='Draw cards until you have 10 cards in your hand.', effect=all_you_can_eat),
        Attack(title='Burst Wheel', cost={T.LIGHTNING: 1, T.COLORLESS: 2}, damage=100, damage_operator='x',
               game_text='Discard all Energy from this Pokemon. This attack does 100 damage for each card you discarded in this way.', effect=burst_wheel),
        Attack(title='Electric Ball', cost={T.LIGHTNING: 1, T.COLORLESS: 2}, damage=160)]


def make_vunion(name, collector_number, *, assembled=False):
    start, kind, hp, weakness, resistance, family, _ = SPECS[name]
    if not start <= collector_number < start + 4:
        raise ValueError('Collector number is not a part of this V-UNION')
    identity = f'CompletePTCGO:Promo_SWSH:{name}VUNION:{"assembled" if assembled else collector_number}'
    abilities = attacks_and_abilities(name) if assembled else [Ability(
        title='Play V-UNION',
        game_text='Once per game, combine 4 different parts from your discard pile onto your Bench.',
        activation=Activations.UNLIMITED, usable_from='discard', is_rule_action=True,
        condition=can_assemble, effect=assemble)]
    card = PokemonCardDef(
        guid=str(uuid.uuid5(uuid.NAMESPACE_URL, identity)) if assembled else NATIVE_GUIDS[collector_number], key='Promo_SWSH',
        name=f'com.direwolfdigital.cake.data.archetypes.pokemon.{name}VUNION.Name',
        display_name=f'{name} V-UNION', searchable_by=[name, f'{name} V-UNION', 'V-UNION'],
        collector_number=collector_number, set_code='Promo_SWSH', rarity=Rarities.RarePromo,
        hp=hp if assembled else 0, elements=[kind], stage=PokemonStage.VUNION,
        retreat_cost=2 if assembled else 0, weakness_type=weakness if assembled else T.UNSET,
        resistance_type=resistance if assembled else T.UNSET, resistance_amount=30,
        family_id=family, subtypes=['V-UNION'], regulation_mark='E',
        attributes={200790: {'type': 'string', 'value': f'SWSH{collector_number}'}},
        abilities=abilities, unplayable_from_hand=True,
        foil=Foil(effects=[FoilEffects.SUNPILLAR], intensity=201))
    card.vunion_name = name
    card.vunion_part = not assembled
    card.vunion_texture = f'{start}to{start + 3}'
    if not assembled:
        # Pieces have no HP, attacks, retreat cost, Weakness or Resistance.
        for attr in (AttrID.HP, AttrID.RETREAT_COST, AttrID.WEAKNESS_TYPES, AttrID.RESISTANCE_TYPES):
            card.extra_attributes.pop(str(attr.value), None)
    return card


def assembled_definition(name):
    if name not in _RUNTIME:
        definition = make_vunion(name, SPECS[name][0], assembled=True)
        CARD_DEFS_BY_GUID.pop(definition.guid)
        RUNTIME_CARD_DEFS_BY_GUID[definition.guid] = definition
        _RUNTIME[name] = definition
    return _RUNTIME[name]


def available_parts(board, player_id, source):
    definition = def_for(source.archetype_id)
    if not getattr(definition, 'vunion_part', False):
        return []
    name = definition.vunion_name
    discard = board.find_player_area(player_id, 'discard')
    if source.parent is not discard or source.owning_player_id != player_id:
        return []
    parts = {definition.collector_number: source}
    for card in discard.children:
        candidate = def_for(card.archetype_id)
        if getattr(candidate, 'vunion_part', False) and candidate.vunion_name == name:
            parts.setdefault(candidate.collector_number, card)
    start = SPECS[name][0]
    return [parts[n] for n in range(start, start + 4)] if len(parts) == 4 else []


class VUnionCard(PokemonCard):
    def to_archetype_attributes(self, download_key):
        attrs = super().to_archetype_attributes(download_key)
        attrs[str(AttrID.IMAGE_URL.value)] = {'type': 'string', 'value': self.combined_texture}
        return attrs


class VUnionPokemonEntity(CompositePokemonEntity):
    def __init__(self, parts):
        definition = assembled_definition(def_for(parts[0].archetype_id).vunion_name)
        raw = definition.to_archetype_dict()
        model = VUnionCard(definition.guid, definition.key, raw['attributes'],
                           definition.display_name, definition.searchable_by, definition.subtypes)
        model.combined_texture = definition.vunion_texture
        super().__init__(model, parts[0].owning_player_id)
        self.physical_parts = tuple(parts)
        self.set_attribute(AttrID.ARCHETYPE_ID, parts[0].archetype_id)
        self.set_attribute(AttrID.COLLECTION_ID, parts[0].archetype_id)

    def serialize(self, viewer_id=None):
        tree = super().serialize(viewer_id)
        tree['archetypeID'] = self.physical_parts[0].archetype_id
        return tree


def can_assemble(board, player_id, source):
    parts = available_parts(board, player_id, source)
    if not parts:
        return False
    name = def_for(source.archetype_id).vunion_name
    state = board.turn_state
    if state is None or (player_id, name) in state.vunion_played:
        return False
    bench = board.find_player_area(player_id, 'bench')
    return (bench is not None and len(bench.children) < effective_bench_capacity(board, player_id)
            and not pokemon_entry_blocked(board, player_id, VUnionPokemonEntity(parts)))


async def assemble(ctx):
    from spirit.game.session.effects import NestedSequence
    if not can_assemble(ctx.board, ctx.player_id, ctx.source):
        return None
    parts = available_parts(ctx.board, ctx.player_id, ctx.source)
    pokemon = VUnionPokemonEntity(parts)
    name = def_for(ctx.source.archetype_id).vunion_name
    ctx.session.turn_state.vunion_played.add((ctx.player_id, name))
    out = ctx.board.find_global_area('outOfPlay')
    bench = ctx.board.find_player_area(ctx.player_id, 'bench')
    slot = ctx.board.free_bench_slot(ctx.player_id)
    out.add_child(pokemon)
    ctx.board._register_entity(pokemon)
    messages = [ctx.session._build_msg(OutboundMsg.ENTITY_ADDED.value, {
        'gameID': ctx.game_id, 'entityID': pokemon.entity_id,
        'owningPlayerID': ctx.player_id, 'parentEntityID': out.entity_id}),
        ctx.session._entity_introduced_msg(pokemon)]
    moves = []
    for index, part in enumerate(parts):
        ctx.board.attach_card(part.entity_id, pokemon.entity_id)
        moves.append(ctx.session._entity_moved_msg(part.entity_id, pokemon.entity_id, index))
    messages.append(NestedSequence(GameSequence.ATTACH_TO_VUNION, moves))
    ctx.board.move_card(pokemon.entity_id, bench.entity_id)
    ctx.session.turn_state.mark_entered_play(pokemon.entity_id)
    messages.append(NestedSequence(GameSequence.PLAY_CARD, [
        ctx.session._entity_moved_msg(pokemon.entity_id, bench.entity_id, slot)]))
    ctx._queue(NestedSequence(GameSequence.CREATE_VUNION, messages),
               bracket=GameSequence.SERIAL_SEQUENCE.value)
    return pokemon


async def refresh_vunion_conditions(session):
    """Antidote Jutsu also removes existing Poison when suppression ends."""
    from spirit.game.session.effects import EffectContext
    from spirit.game.session.passives import conditions_blocked
    for pid in session.players:
        pokemon = session.board_state.active_pokemon(pid)
        if not isinstance(pokemon, VUnionPokemonEntity):
            continue
        if 'Poisoned' not in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            continue
        if conditions_blocked(session.board_state, pokemon, SpecialConditions.POISONED):
            ctx = EffectContext(session, pid, pokemon, None)
            await ctx.cure_condition(pokemon, SpecialConditions.POISONED)
            await ctx.flush_choreography()
