from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9dfdaa5-7a53-5009-8a3b-fa27beed8a7d',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name',
    display_name='Herdier',
    searchable_by=['Herdier', 'Stage 1', 'Herdier'],
    subtypes=['Stage 1'],
    collector_number=104,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name',
    family_id=506,
    abilities=[
        Ability(
            title='Treasure Hunt',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put an Item card from your discard pile into your hand.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
