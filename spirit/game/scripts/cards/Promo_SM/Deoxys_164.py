from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c8af6223-78de-5f42-82c1-94e23bad39da',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name',
    display_name='Deoxys',
    searchable_by=['Deoxys', 'Basic', 'Deoxys'],
    subtypes=['Basic'],
    collector_number=164,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=386,
    abilities=[
        Ability(
            title='Power Suction',
            game_text='Once during your turn (before your attack), you may move an Energy from 1 of your Pokémon to 1 of your Deoxys.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Psycho Boost',
            game_text="During your next turn, this Pokémon's Psycho Boost attack's base damage is 50.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
