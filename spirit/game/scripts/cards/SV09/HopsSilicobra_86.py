from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="b5945090-2b62-515d-ad53-3c59da5a9458",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSilicobra.Name",
    display_name="Hop's Silicobra",
    searchable_by=["Hop's Silicobra", "Basic", "HopsSilicobra"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=843,
    abilities=[
        Attack(
            title="Turf Maker",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
