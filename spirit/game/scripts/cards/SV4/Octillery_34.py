from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e708f52-bd5c-5e2c-b417-d468a17861ee',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name',
    display_name='Octillery',
    searchable_by=['Octillery', 'Stage 1', 'Octillery'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name',
    family_id=223,
    abilities=[
        Ability(
            title='Suction Cup Draw',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may draw 3 cards.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Smokescreen Shot',
            game_text="During your opponent's next turn, if the Defending Pokémon tries to use an attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
