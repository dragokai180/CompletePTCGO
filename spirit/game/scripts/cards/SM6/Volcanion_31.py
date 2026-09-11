from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='976c1a05-3eeb-5d87-9bc2-3d3ee0553b67',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name',
    display_name='Volcanion ◇',
    searchable_by=['Volcanion ◇', 'Basic', 'Prism Star', 'Volcanion'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=31,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=721,
    abilities=[
        Ability(
            title='Jet Geyser',
            game_text='Once during your turn (before your attack), you may discard a Water Energy card from your hand. If you do, your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Sauna Blast',
            game_text="This attack does 20 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
