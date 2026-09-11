from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="18b7a53b-3502-504a-a8e8-268fdb2ab8f7",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Okidogiex.Name",
    display_name="Okidogi ex",
    searchable_by=["Okidogi ex", "Basic", "ex", "Okidogiex"],
    subtypes=["Basic", "ex"],
    collector_number=36,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=1014,
    abilities=[
        Attack(
            title="Poisonous Musculature",
            game_text="Search your deck for up to 2 Basic Darkness Energy cards and attach them to this Pokémon. Then, shuffle your deck. If you attached Energy to a Pokémon in this way, this Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Chain-Crazed",
            game_text="If this Pokémon is Poisoned, this attack does 130 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
