from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0553685d-34ad-527a-afd0-e0aa35647894',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name',
    display_name='Marowak',
    searchable_by=['Marowak', 'Stage 1', 'Marowak'],
    subtypes=['Stage 1'],
    collector_number=91,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    family_id=104,
    abilities=[
        Attack(
            title='Bone Rush',
            game_text='Flip a coin until you get tails. This attack does 50 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Assault Boom',
            game_text="If your opponent's Active Pokémon has a Pokémon Tool card attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
