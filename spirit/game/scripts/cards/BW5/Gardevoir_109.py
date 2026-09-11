from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import lost_zone_from_opponent_discard
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def mind_shock(ctx):
    """60. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)



card = PokemonCardDef(
    guid="bbb64b16-321e-5d5a-9469-0eebfe5900cb",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir","Stage 2","Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=109,
    set_code="BW5",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    abilities=[
        Ability(
            title="Psychic Mirage",
            game_text="Each basic Psychic Energy attached to your Psychic Pokémon provides PsychicPsychic Energy. You can't apply more than 1 Psychic Mirage Ability at a time.",
            passive=bw_legacy_passive("Each basic Psychic Energy attached to your Psychic Pokémon provides PsychicPsychic Energy. You can't apply more than 1 Psychic Mirage Ability at a time."),
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=mind_shock,
        ),
    ],
)
