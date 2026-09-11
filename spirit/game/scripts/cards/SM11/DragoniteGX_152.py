from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='423df2bf-3232-5fc7-89ef-c724e0fe8191',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteGX.Name',
    display_name='Dragonite-GX',
    searchable_by=['Dragonite-GX', 'Stage 2', 'GX', 'DragoniteGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=152,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title='Sky Judgment',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 5},
            damage=270,
            effect=standard_attack,
        ),
        Attack(
            title='Mach Delivery-GX',
            game_text="You may discard any number of cards from your hand until you have 9 or fewer. Draw cards until you have 10 cards in your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
