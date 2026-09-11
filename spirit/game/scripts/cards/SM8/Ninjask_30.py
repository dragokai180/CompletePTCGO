from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dac17095-31e2-5371-971a-8c5801de5928',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name',
    display_name='Ninjask',
    searchable_by=['Ninjask', 'Stage 1', 'Ninjask'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name',
    family_id=290,
    abilities=[
        Ability(
            title='Molting',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put a Shedinja from your discard pile onto your Bench.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='X-Scissor',
            game_text='Flip a coin. If heads, this attack does 40 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
