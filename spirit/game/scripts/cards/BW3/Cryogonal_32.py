from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="d352ae53-b4c7-5036-b13d-fa876efdf0ff",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal","Basic","Cryogonal"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Attack(
            title="Icy Wind",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=powder_snow,
        ),
        Attack(
            title="Ice Shard",
            game_text="If the Defending Pokémon is a Fighting Pokémon, this attack does 40 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
