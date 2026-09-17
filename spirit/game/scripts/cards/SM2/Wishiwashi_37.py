from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e99b05f9-ce13-5ac0-94ff-1bb89ea4e402',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name',
    display_name='Wishiwashi',
    searchable_by=['Wishiwashi', 'Basic', 'Wishiwashi'],
    subtypes=['Basic'],
    collector_number=37,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=746,
    abilities=[
        Ability(
            title='Schooling',
            game_text='Once during your turn (before your attack), you may switch this Pokémon with a Wishiwashi-GX in your hand. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Sharpshooting',
            game_text="This attack does 10 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
