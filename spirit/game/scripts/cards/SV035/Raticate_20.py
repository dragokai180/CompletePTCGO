from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1cc8ec87-f134-5634-b934-cc9211dad663',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name',
    display_name='Raticate',
    searchable_by=['Raticate', 'Stage 1', 'Raticate'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    family_id=19,
    abilities=[
        Attack(
            title='Second Bite',
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
