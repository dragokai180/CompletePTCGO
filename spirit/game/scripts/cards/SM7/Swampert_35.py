from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c924747e-8a7c-565f-8799-9b93a52e61e6',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name',
    display_name='Swampert',
    searchable_by=['Swampert', 'Stage 2', 'Swampert'],
    subtypes=['Stage 2'],
    collector_number=35,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name',
    family_id=258,
    abilities=[
        Ability(
            title='Power Draw',
            game_text='Once during your turn (before your attack), you may discard a card from your hand. If you do, draw 3 cards.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hydro Pump',
            game_text='This attack does 20 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
