from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6a757103-0d9c-5b9b-a823-253de6f56311',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SylveonGX.Name',
    display_name='Sylveon-GX',
    searchable_by=['Sylveon-GX', 'Stage 1', 'GX', 'SylveonGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=92,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=700,
    abilities=[
        Attack(
            title='Magical Ribbon',
            game_text='Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title='Plea-GX',
            game_text="Put 2 of your opponent's Benched Pokémon and all cards attached to them into your opponent's hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
