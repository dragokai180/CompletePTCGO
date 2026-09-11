from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="b9b1be01-eb6d-5106-9603-7ecb0904be43",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    display_name="Cubchoo",
    searchable_by=["Cubchoo","Basic","Cubchoo"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Attack(
            title="Sniffle",
            game_text="During your next turn, this Pokémon's Belt attack's base damage is 40.",
            cost={PokemonTypes.WATER: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Belt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
