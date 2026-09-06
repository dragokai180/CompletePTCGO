from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="923d11c3-7941-5e5b-b304-f263f150cfa7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesImpidimp.Name",
    display_name="Marnie's Impidimp",
    searchable_by=["Marnie's Impidimp", "Basic", "MarniesImpidimp"],
    subtypes=["Basic"],
    collector_number=134,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=859,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(1),
        ),
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
