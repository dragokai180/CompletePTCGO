from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='17093d99-d181-59bb-b059-1b23fe9cd71d',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name',
    display_name='Shinx',
    searchable_by=['Shinx', 'Basic', 'Shinx'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=403,
    abilities=[
        Ability(
            title='Big Roar',
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may switch out your opponent's Active Pokémon to the Bench.\xa0(Your opponent chooses the new Active Pokémon.)",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
