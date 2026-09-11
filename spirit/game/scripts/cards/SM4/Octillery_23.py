from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dcf08b92-6ed3-561a-8a4b-c861d210bc11',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name',
    display_name='Octillery',
    searchable_by=['Octillery', 'Stage 1', 'Octillery'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name',
    family_id=223,
    abilities=[
        Attack(
            title='Ink Spit',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Special Artillery',
            game_text='You may discard a Special Energy from this Pokémon. If you do, this attack does 80 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
