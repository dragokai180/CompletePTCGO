from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='50ea346f-fd23-5e30-ae8c-297ca0b75c17',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Komala.Name',
    display_name='Komala',
    searchable_by=['Komala', 'Basic', 'Komala'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=775,
    abilities=[
        Ability(
            title='Comatose',
            game_text='As long as this Pokémon is your Active Pokémon, whenever you attach an Energy from your hand to it, it is now Asleep.',
            passive=standard_passive('As long as this Pokémon is your Active Pokémon, whenever you attach an Energy from your hand to it, it is now Asleep.'),
        ),
        Attack(
            title='Hypno Roll',
            game_text='This attack can be used if this Pokémon is Asleep. If it is not Asleep, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
