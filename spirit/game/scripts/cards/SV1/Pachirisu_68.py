from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0dc7af0a-687e-5388-8e9c-6cbf8112c5fc',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name',
    display_name='Pachirisu',
    searchable_by=['Pachirisu', 'Basic', 'Pachirisu'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=417,
    abilities=[
        Ability(
            title='Electricity Pouches',
            game_text="This Pokémon can't be Paralyzed.",
            passive=standard_passive("This Pokémon can't be Paralyzed."),
        ),
        Attack(
            title='Everyone Discharge',
            game_text="This attack does 20 more damage for each of your Benched Lightning Pokémon. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
