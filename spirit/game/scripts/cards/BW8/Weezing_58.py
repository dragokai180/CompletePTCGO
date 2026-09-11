from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, named_in_play, spread_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="708b2bb5-1a8f-5ae8-bf2e-2644c26fd7a1",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing","Stage 1","Weezing"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    abilities=[
        Ability(
            title="Aftermath",
            game_text="When this Pokémon is Knocked Out by damage from an opponent's attack, discard the top 3 cards of your opponent's deck.",
            trigger="on_knocked_out",
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Smogbank",
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=spread_damage(20, side="opponent"),
        ),
    ],
)
