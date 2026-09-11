from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='64ec2711-8690-55d6-a6f3-23d77b158593',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name',
    display_name='Milotic',
    searchable_by=['Milotic', 'Stage 1', 'Milotic'],
    subtypes=['Stage 1'],
    collector_number=44,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name',
    family_id=349,
    abilities=[
        Ability(
            title='Sparkling Ripples',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may put a card from your discard pile into your hand.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Aqua Swirl',
            game_text='You may have your opponent switch his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
