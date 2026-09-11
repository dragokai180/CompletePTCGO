from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7cb43e5e-f796-5cb3-b464-eb3c857a96c9',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Klawf.Name',
    display_name='Klawf',
    searchable_by=['Klawf', 'Basic', 'Klawf'],
    subtypes=['Basic'],
    collector_number=105,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=950,
    abilities=[
        Attack(
            title='Unhinged Scissors',
            game_text='If this Pokémon is affected by a Special Condition, this attack does 160 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Boiled Press',
            game_text='This Pokémon is now Burned.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
