from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)



card = PokemonCardDef(
    guid='d557deb4-aed6-5247-b373-6e8052e102ad',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LucarioVSTAR.Name',
    display_name='Lucario VSTAR',
    searchable_by=['Lucario VSTAR', 'VSTAR', 'LucarioVSTAR'],
    subtypes=['VSTAR'],
    collector_number=214,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH214'}},
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.LucarioV.Name',
    family_id=448,
    abilities=[
        Attack(
            title='Fighting Knuckle',
            game_text="If your opponent's Active Pokémon is a Pokémon V, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Aura Star',
            vstar=True,
            game_text="This attack does 70 damage for each Energy attached to all of your opponent's Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
