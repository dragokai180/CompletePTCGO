from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ad306bb-9cb7-5980-af76-4120b67107f4',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name',
    display_name='Dugtrio',
    searchable_by=['Dugtrio', 'Stage 1', 'Dugtrio'],
    subtypes=['Stage 1'],
    collector_number=86,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    family_id=50,
    abilities=[
        Attack(
            title='Home Ground',
            game_text='If you have any Stadium card in play, this attack does 60 more damage.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
