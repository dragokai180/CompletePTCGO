from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f4757da-5434-5647-bed8-8b489219074f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name',
    display_name='Spiritomb',
    searchable_by=['Spiritomb', 'Basic', 'Spiritomb'],
    subtypes=['Basic'],
    collector_number=129,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=442,
    abilities=[
        Attack(
            title='Taunt',
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Doom Decree',
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pokémon is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=standard_attack,
        ),
    ],
)
