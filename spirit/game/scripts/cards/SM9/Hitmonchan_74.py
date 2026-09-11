from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='89e485d1-dcda-56de-ba57-ec4d8d8cca96',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name',
    display_name='Hitmonchan',
    searchable_by=['Hitmonchan', 'Basic', 'Hitmonchan'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=107,
    abilities=[
        Attack(
            title='Hit and Run',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Magnum Punch',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
