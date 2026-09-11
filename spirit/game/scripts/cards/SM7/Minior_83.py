from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='62782593-fb01-574b-8fbc-fe20a14a2f4a',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name',
    display_name='Minior',
    searchable_by=['Minior', 'Basic', 'Minior'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=774,
    abilities=[
        Ability(
            title='Falling Star',
            game_text="Once during your turn (before your attack), if this Pokémon is in your hand and your Bench isn't full, you may move your Active Pokémon to your Bench and play this Pokémon as your new Active Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Swift',
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
