from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f35c9970-1dd4-5f9d-acb7-db8381be0adf',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name',
    display_name='Flamigo',
    searchable_by=['Flamigo', 'Basic', 'Flamigo'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title='Combat Beak',
            game_text="This attack does 20 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
