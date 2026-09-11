from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e15acfdc-cdc2-5218-a976-e76c0e61bcda',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name',
    display_name='Anorith',
    searchable_by=['Anorith', 'Restored', 'Anorith'],
    subtypes=['Restored'],
    collector_number=56,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.RESTORED,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.ClawFossilAnorith.Name',
    family_id=347,
    abilities=[
        Ability(
            title='Restored Barrier',
            game_text='Each of your Restored Pokémon has no Weakness.',
            passive=standard_passive('Each of your Restored Pokémon has no Weakness.'),
        ),
        Attack(
            title='X-Scissor',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
