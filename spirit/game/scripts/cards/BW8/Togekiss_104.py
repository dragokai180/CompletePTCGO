from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="3e41a8a1-1ef1-50f3-8e4a-23d4f056cd95",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss","Stage 2","Togekiss"],
    subtypes=["Stage 2"],
    collector_number=104,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    abilities=[
        Ability(
            title="Bright Veil",
            game_text="As long as this Pokémon is your Active Pokémon, whenever your opponent plays an Item card from his or her hand, prevent all effects of that card done to your Pokémon.",
            passive=bw_legacy_passive("As long as this Pokémon is your Active Pokémon, whenever your opponent plays an Item card from his or her hand, prevent all effects of that card done to your Pokémon."),
        ),
        Attack(
            title="Return",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=draw_until_effect(6),
        ),
    ],
)
