from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0e4c292b-ba5d-5b69-8bb2-42fee7f9b8df',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanNinetales.Name',
    display_name='Alolan Ninetales',
    searchable_by=['Alolan Ninetales', 'Stage 1', 'AlolanNinetales'],
    subtypes=['Stage 1'],
    collector_number=145,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name',
    family_id=37,
    abilities=[
        Attack(
            title='Rubbish Blizzard',
            game_text='This attack does 10 damage for each Pokémon Tool card in your discard pile.',
            cost={},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
