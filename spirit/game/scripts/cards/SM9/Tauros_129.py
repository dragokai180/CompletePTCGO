from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1e68ed63-df71-5fa1-9044-c774da4f5e70',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name',
    display_name='Tauros',
    searchable_by=['Tauros', 'Basic', 'Tauros'],
    subtypes=['Basic'],
    collector_number=129,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=128,
    abilities=[
        Attack(
            title='Raging Herd',
            game_text='This attack does 10 more damage for each damage counter on all of your Tauros and Tauros-GX.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
