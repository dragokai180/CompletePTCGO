from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c6dcaf69-e5b6-5ff1-bb9b-d804cc1bd25d',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaichu.Name',
    display_name='Alolan Raichu',
    searchable_by=['Alolan Raichu', 'Stage 1', 'AlolanRaichu'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    family_id=25,
    abilities=[
        Ability(
            title='Surge Surfer',
            game_text='If there is any Stadium card in play, this Pokémon has no Retreat Cost.',
            passive=standard_passive('If there is any Stadium card in play, this Pokémon has no Retreat Cost.'),
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
