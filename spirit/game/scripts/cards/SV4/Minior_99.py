from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b8fed851-546a-5873-845a-4e76943c60cc',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name',
    display_name='Minior',
    searchable_by=['Minior', 'Basic', 'Minior'],
    subtypes=['Basic'],
    collector_number=99,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=774,
    abilities=[
        Ability(
            title='Far-Flying Meteor',
            game_text='Once during your turn, if this Pokémon is on your Bench, when you attach an Energy card from your hand to this Pokémon, you may switch it with your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Gravitational Tackle',
            game_text="This attack does 20 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
