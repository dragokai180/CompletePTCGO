from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="36a18b62-338a-5b75-9b8b-d75c6db60f44",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal","Basic","Cryogonal","Team Plasma"],
    subtypes=["Basic","Team Plasma"],
    collector_number=30,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Attack(
            title="Call Sign",
            game_text="Search your deck for a Water Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Cryofreeze",
            game_text="Discard an Energy attached to this Pokémon. The Defending Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=bw_legacy_attack,
        ),
    ],
)
