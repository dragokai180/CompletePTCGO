from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import knock_off, reinforced_lariat
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="fe40f556-61fb-52fe-98f9-c1105898b0ac",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow","Stage 1","Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="You may have your opponent switch the Defending Pokémon with 1 of his or her Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Diving Swipe",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=knock_off,
        ),
    ],
)
