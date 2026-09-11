from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='74d642b2-9344-5bc4-8e8e-f32f77fe4d28',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Emboar.Name',
    display_name='Emboar',
    searchable_by=['Emboar', 'Stage 2', 'Emboar'],
    subtypes=['Stage 2'],
    collector_number=33,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name',
    family_id=498,
    abilities=[
        Ability(
            title='Explosive Fire Dance',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may look at the top 8 cards of your deck and attach any number of basic Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
    ],
)
