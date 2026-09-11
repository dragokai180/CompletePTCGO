from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='add2c2e5-4cbf-5502-ae83-55bbc977e92f',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslash.Name',
    display_name='Alolan Sandslash',
    searchable_by=['Alolan Sandslash', 'Stage 1', 'AlolanSandslash'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name',
    family_id=28,
    abilities=[
        Ability(
            title='Slush Rush',
            game_text='Once during your turn (before your attack), you may draw a card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Smash Turn',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
