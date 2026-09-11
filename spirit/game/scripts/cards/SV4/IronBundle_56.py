from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4842f7a3-9e1b-51c7-8574-30d370db9f2b',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.IronBundle.Name',
    display_name='Iron Bundle',
    searchable_by=['Iron Bundle', 'Basic', 'Future', 'IronBundle'],
    subtypes=['Basic', 'Future'],
    collector_number=56,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=991,
    abilities=[
        Ability(
            title='Hyper Blower',
            game_text="Once during your turn, if this Pokémon is on your Bench, you may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.) If you do, discard this Pokémon and all attached cards.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Refrigerated Stream',
            game_text="If the Defending Pokémon is an Evolution Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
