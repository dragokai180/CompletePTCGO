from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6fce7a9d-eb00-54f5-a56f-d6bd85ce42cd',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name',
    display_name='Malamar',
    searchable_by=['Malamar', 'Stage 1', 'Malamar'],
    subtypes=['Stage 1'],
    collector_number=58,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name',
    family_id=687,
    abilities=[
        Ability(
            title='Contrary',
            game_text='If this Pokémon is your Active Pokémon, whenever your opponent flips a coin during his or her turn, treat it as tails.',
            passive=standard_passive('If this Pokémon is your Active Pokémon, whenever your opponent flips a coin during his or her turn, treat it as tails.'),
        ),
        Attack(
            title='Conform',
            game_text="If you have the same number of cards in your hand as your opponent, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."),
)
