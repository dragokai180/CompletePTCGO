from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a577185-ead9-5f77-a4dc-51543dfa10a6',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SuicuneGX.Name',
    display_name='Suicune-GX',
    searchable_by=['Suicune-GX', 'Basic', 'GX', 'SuicuneGX'],
    subtypes=['Basic', 'GX'],
    collector_number=60,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=245,
    abilities=[
        Ability(
            title='Phantom Winds',
            game_text='Once during your turn (before your attack), if this Pokémon is on your Bench, you may shuffle it and all cards attached to it into your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Cure Stream',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Brinicles-GX',
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
