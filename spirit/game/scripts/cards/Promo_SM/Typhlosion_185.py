from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c93b688-3f3d-59a9-8916-06b8fb21dbb0',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name',
    display_name='Typhlosion',
    searchable_by=['Typhlosion', 'Stage 2', 'Typhlosion'],
    subtypes=['Stage 2'],
    collector_number=185,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name',
    family_id=157,
    abilities=[
        Attack(
            title='Exploder',
            game_text='Search your deck for up to 3 Fire Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bursting Inferno',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
