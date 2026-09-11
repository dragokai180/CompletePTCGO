from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4604c2d-41af-554b-b871-036902cd0fd2',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name',
    display_name='Giratina',
    searchable_by=['Giratina', 'Basic', 'Giratina'],
    subtypes=['Basic'],
    collector_number=151,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=487,
    abilities=[
        Ability(
            title='Distortion Door',
            game_text="Once during your turn (before your attack), if this Pokémon is in your discard pile, you may put it onto your Bench. If you do, put 1 damage counter on 2 of your opponent's Benched Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
            usable_from='discard',
        ),
        Attack(
            title='Shadow Impact',
            game_text='Put 4 damage counters on 1 of your Pokémon.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
