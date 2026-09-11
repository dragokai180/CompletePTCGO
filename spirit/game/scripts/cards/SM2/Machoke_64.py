from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bccb0b1b-2f13-530b-b07b-3fbbf6d17fb5',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name',
    display_name='Machoke',
    searchable_by=['Machoke', 'Stage 1', 'Machoke'],
    subtypes=['Stage 1'],
    collector_number=64,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name',
    family_id=66,
    abilities=[
        Ability(
            title='Daunting Pose',
            game_text="Prevent all damage done to your Benched Pokémon by your opponent's attacks. Your opponent's attacks and Abilities can't put damage counters on your Benched Pokémon.",
            passive=standard_passive("Prevent all damage done to your Benched Pokémon by your opponent's attacks. Your opponent's attacks and Abilities can't put damage counters on your Benched Pokémon."),
        ),
        Attack(
            title='Cross Chop',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
