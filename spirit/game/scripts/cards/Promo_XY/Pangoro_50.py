from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bcff5285-5bf5-58ff-811c-ecc1b0c9719e',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name',
    display_name='Pangoro',
    searchable_by=['Pangoro', 'Stage 1', 'Pangoro'],
    subtypes=['Stage 1'],
    collector_number=50,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name',
    family_id=675,
    abilities=[
        Ability(
            title='Benevolent Boss',
            game_text='If this Pokémon is your Active Pokémon, it gets +20 HP for each of your Benched Pokémon.',
            passive=standard_passive('If this Pokémon is your Active Pokémon, it gets +20 HP for each of your Benched Pokémon.'),
        ),
        Attack(
            title='Crazy Knuckle',
            game_text='If this Pokémon is affected by a Special Condition, this attack does 40 more damage.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
