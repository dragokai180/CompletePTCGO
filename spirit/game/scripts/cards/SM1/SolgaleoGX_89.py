from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3affb8cc-7c65-5f39-a60f-b7bc70395df8',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoGX.Name',
    display_name='Solgaleo-GX',
    searchable_by=['Solgaleo-GX', 'Stage 2', 'GX', 'SolgaleoGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=89,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    family_id=789,
    abilities=[
        Ability(
            title='Ultra Road',
            game_text='Once during your turn (before your attack), you may switch your Active Pokémon with 1 of your Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Sunsteel Strike',
            game_text='Discard all Energy from this Pokémon.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=standard_attack,
        ),
        Attack(
            title='Sol Burst-GX',
            game_text="Search your deck for up to 5 Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
