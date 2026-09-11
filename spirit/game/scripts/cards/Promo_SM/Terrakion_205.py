from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='66c5a872-4438-5b2e-a069-40e34bbaca10',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Terrakion.Name',
    display_name='Terrakion',
    searchable_by=['Terrakion', 'Basic', 'Terrakion'],
    subtypes=['Basic'],
    collector_number=205,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=639,
    abilities=[
        Attack(
            title='Cavern Counter',
            game_text='If all of your Benched Pokémon have at least 1 damage counter on them, this attack does 150 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Boulder Crush',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)
