from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6230fe74-10ce-5ca5-a30e-f7d21837a1cf",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensSkwovet.Name",
    display_name="Arven's Skwovet",
    searchable_by=["Arven's Skwovet", "Basic", "ArvensSkwovet"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=819,
    abilities=[
        Attack(
            title="Gnaw Through",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
