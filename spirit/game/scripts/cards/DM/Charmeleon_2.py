from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5a81ab86-4aec-5262-9160-78027cb80bd9',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    display_name='Charmeleon',
    searchable_by=['Charmeleon', 'Stage 1', 'Charmeleon'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    family_id=4,
    abilities=[
        Ability(
            title='Burning Fighter',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may discard the top 5 cards of your deck. If any of those cards are Fire Energy cards, attach them to this Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
