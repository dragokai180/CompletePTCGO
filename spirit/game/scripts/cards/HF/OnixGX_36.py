from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='36d88b05-9a07-5c2f-8c54-7254e61e512e',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.OnixGX.Name',
    display_name='Onix-GX',
    searchable_by=['Onix-GX', 'Basic', 'GX', 'OnixGX'],
    subtypes=['Basic', 'GX'],
    collector_number=36,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=95,
    abilities=[
        Attack(
            title='Bind',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 4},
            damage=150,
        ),
        Attack(
            title='Rocky Avalanche-GX',
            game_text="During your opponent's next turn, this Pokémon takes 100 less damage from attacks (after applying Weakness and Resistance). (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=standard_attack,
            locks_next_turn=True,
            gx=True,
        ),
    ],
)
