from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="7f8c299a-09ef-5aeb-9550-bed55bbc9f82",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal","Basic","Cryogonal"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Attack(
            title="Ice Chain",
            game_text="Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.WATER: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Frost Vanish",
            game_text="You may return this Pokémon and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=bw_legacy_attack,
        ),
    ],
)
